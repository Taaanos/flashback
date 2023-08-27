import unittest
import os
import tempfile
import time
from video_pool import create_video_pool, sort_videos


class TestCreateVideoPool(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.folder_path = self.test_dir.name

        # Create some test files with different extensions
        self.mp4_files = ['video1.mp4', 'video2.mp4']
        self.avi_files = ['video1.avi', 'video2.avi']
        for file_name in self.mp4_files + self.avi_files:
            open(os.path.join(self.folder_path, file_name), 'w').close()

    def tearDown(self):
        self.test_dir.cleanup()

    def test_create_video_pool_with_mp4(self):
        result = create_video_pool([self.folder_path], 'mp4')
        expected = [os.path.join(self.folder_path, file) for file in self.mp4_files]
        self.assertEqual(set(result), set(expected))

    def test_create_video_pool_with_avi(self):
        result = create_video_pool([self.folder_path], 'avi')
        expected = [os.path.join(self.folder_path, file) for file in self.avi_files]
        self.assertEqual(set(result), set(expected))

    def test_create_video_pool_with_no_match(self):
        result = create_video_pool([self.folder_path], 'mkv')
        self.assertEqual(result, [])


class TestSortVideos(unittest.TestCase):

    def setUp(self):
        # Create temporary directory and video files
        self.temp_dir = tempfile.TemporaryDirectory()

        self.video1 = os.path.join(self.temp_dir.name, "video1.mp4")
        self.video2 = os.path.join(self.temp_dir.name, "video2.mp4")
        self.video3 = os.path.join(self.temp_dir.name, "video3.mp4")

        open(self.video1, 'a').close()
        open(self.video2, 'a').close()
        open(self.video3, 'a').close()

        # Set modification times
        os.utime(self.video1, (time.time() - 60, time.time() - 60))
        os.utime(self.video2, (time.time() - 30, time.time() - 30))
        os.utime(self.video3, (time.time(), time.time()))

        self.video_list = [self.video1, self.video2, self.video3]

    def tearDown(self):
        # Clean up temporary directory
        self.temp_dir.cleanup()

    def test_sort_videos_seq(self):
        sorted_list = sort_videos(self.video_list, 'seq')
        self.assertEqual(sorted_list, [self.video1, self.video2, self.video3])

    def test_sort_videos_rand(self):
        random_list = sort_videos(self.video_list, 'rand')
        self.assertNotEqual(random_list, [self.video1, self.video2, self.video3])

    def test_sort_videos_invalid(self):
        invalid_list = sort_videos(self.video_list, 'invalid')
        self.assertEqual(invalid_list, self.video_list)


if __name__ == '__main__':
    unittest.main()
