class MoodAnalyser:
    def mood_analyser(self, msg: str) -> str:
        words = ('веселое', 'грустное', 'счастливое')
        for word in words:
            if word in msg:
                return word

        return 'неизвестное'
