"""A video player class."""

from .video_library import VideoLibrary
import random as rnd
from .video_playlist import Playlist


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.extra_items = {}
        self.playlists = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        
#         video_dict = {}
#         video_file = open(self.videos)
#         for line in video_file:
#             name, video_id, hashtags = line.split("|")
#             video_dict[name] = (video_id, hashtags)
            
#         for video in video_dict:
#             print(video + "("+video_dict[video][0] + ") [" + video_dict[video][1] + "]")

#         print("show_all_videos needs implementation")

        print("Here's a list of all available videos:")
    
        ordered_videos = []

        for video in self._video_library.get_all_videos():
#             for i in range(len(video.tags)):
#                 tag_string = "["
            ordered_videos.append(f"{video.title} ({video.video_id}) [{' '.join(video.tags)}]")
        
        ordered_videos.sort()
        
        for video in ordered_videos:
            print(f'\t {video}')
            
            
    def all_playing(self):
        "Return video object current playing"
        videos = self._video_library.get_all_videos()
        for v in videos:
            if v._status == 1:
                return(v)
        return(None)

    def all_paused(self):
        "Return video object current playing"
        videos = self._video_library.get_all_videos()
        for v in videos:
            if v._status == 2:
                return(v)
        return(None)
            

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
#         print("play_video needs implementation")

#         for video in self._video_library.get_all_videos():
        
#             (f"{video.video_id}_playing") = False
#             d["{}_playing".format(video.video_id)] = False
#             exec(f'{video.video_id}_playing = False')
            
#         nothing_playing = True
        
#         if nothing_playing == True:
#             d["{}_playing".format(self.video_id)] = True
#             exec(f'{self.video_id}_playing = True')
#             exec(f'{video.id}_playing = True')
#             nothing_playing = False
            
#             print(f"Playing video: {self.title}")

        video = self._video_library.get_video(video_id)
        if video is None:
            print("Cannot play video: Video does not exist")
        else:
            if self.all_playing() is not None:
                print("Stopping video: {}".format(self.all_playing()._title))
                self.all_playing()._status = 0
            elif self.all_paused() is not None:
                print("Stopping video: {}".format(self.all_paused()._title))
                self.all_paused()._status = 0
            print("Playing video: {}".format(video._title))
            video._status = 1
        #print("play_video needs implementation")

        

    def stop_video(self):
        """Stops the current video."""
       
        
        if self.all_playing() is not None:
            print("Stopping video: {}".format(self.all_playing()._title))
            self.all_playing()._status = 0
            return(None)
            
        if self.all_paused() is not None:
            print("Stopping video: {}".format(self.all_paused()._title))
            self.all_paused()._status = 0
            return(None)
            
        if self.all_playing() == None and self.all_paused() == None:
            print("Cannot stop video: No video is currently playing")
            return(None)
            
            

#         print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""
        
        if self.all_playing() is not None:
            print("Stopping video: {}".format(self.all_playing()._title))
            self.all_playing()._status = 0
        if self.all_paused() is not None:
            print("Stopping video: {}".format(self.all_paused()._title))
            self.all_paused()._status = 0
            
        randomint = rnd.randint(0,len(self._video_library.get_all_videos())-1)
        video = self._video_library.get_all_videos()[randomint]
        print("Playing video: {}".format(video._title))
        video._status = 1

#         print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        
        if self.all_paused() is not None:
            print("Video already paused: {}".format(self.all_paused()._title))
            
        if self.all_playing() is not None:
            print("Pausing video: {}".format(self.all_playing()._title))
            self.all_playing()._status = 2
            
        if self.all_playing() == None and self.all_paused() == None:
            print("Cannot pause video: No video is currently playing")

#         print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""
        
        if self.all_playing() is not None:
            print("Cannot continue video: Video is not paused")
            
        if self.all_paused() is not None:
            print("Continuing video: {}".format(self.all_paused()._title))
            self.all_paused()._status = 1
            
        if self.all_playing() == None and self.all_paused() == None:
            print("Cannot continue video: No video is currently playing")

#         print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        
        if self.all_paused() is not None:
            print("Currently playing: {} ({}) [{}] - PAUSED".format(self.all_paused()._title, self.all_paused()._video_id, ' '.join(self.all_paused()._tags)))
            
        if self.all_playing() is not None:
            print("Currently playing: {} ({}) [{}]".format(self.all_playing()._title, self.all_playing()._video_id, ' '.join(self.all_playing()._tags)))
            
        if self.all_playing() == None and self.all_paused() == None:
            print("No video is currently playing")

#         print("show_playing needs implementation")



    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        
        new_playlist_id = playlist_name.lower()
        if new_playlist_id in self.playlists.keys():
            print("Cannot create playlist: A playlist with the same name already exists")
            return
        
        new_playlist = Playlist(playlist_name)
        self.playlists[new_playlist_id] = new_playlist
        print(f"Successfully created new playlist: {playlist_name}")
        
#         print("create_playlist needs implementation")



    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
