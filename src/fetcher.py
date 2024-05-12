from __init__ import *


class Fetcher:
    def __init__(self, keyword) -> None:
        self.keyword = keyword

    def fetch(self) -> CustomSearch:
        return CustomSearch(self.keyword, VideoUploadDateFilter.lastHour, limit=20)
