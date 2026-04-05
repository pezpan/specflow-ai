class VaguenessGuard:
    """
    Detects vague or insufficient user input.
    """
    def __init__(self, min_words: int = 3):
        self.min_words = min_words
        self.vague_keywords = [
            "don't know", "no sé", 
            "whatever", "lo que sea",
            "you decide", "tú decides",
            "maybe", "quizás"
        ]

    def is_vague(self, text: str) -> bool:
        """
        Returns True if the text is considered vague.
        """
        if not text or not text.strip():
            return True
            
        words = text.split()
        if len(words) < self.min_words:
            return True
            
        text_lower = text.lower()
        for kw in self.vague_keywords:
            if kw in text_lower:
                return True
                
        return False
