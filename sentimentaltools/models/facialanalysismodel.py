class facial_analysis_model():

    related_bounding_box_id = None
    emotions = None
    dominant_emotion = None
    location_data = None
    related_frame = None
    analyzed_frame = None

    def get_related_bounding_box_id(self):
        return self.related_bounding_box_id

    def get_emotions(self):
        return self.emotions

    def get_dominant_emotion(self):
        return self.dominant_emotion

    def get_location_data(self):
        return self.location_data

    def get_related_frame(self):
        return self.related_frame

    def get_analyzed_frame(self):
        return self.analyzed_frame

    def set_related_bounding_box_id(self, related_bounding_box_id):
        self.related_bounding_box_id = related_bounding_box_id

    def set_emotions(self, emotions):
        self.emotions = emotions

    def set_dominant_emotion(self, dominant_emotion):
        self.dominant_emotion = dominant_emotion

    def set_location_data(self, location_data):
        self.location_data = location_data

    def set_related_frame(self, related_frame):
        self.related_frame = related_frame

    def set_analyzed_frame(self, analyzed_frame):
        self.analyzed_frame = analyzed_frame