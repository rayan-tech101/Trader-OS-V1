# streak_analysis.py

class StreakAnalyzer:
    def __init__(self):
        self.winning_streak = 0
        self.losing_streak = 0
        self.history = []

    def record_result(self, result: str):
        """Record the result of a trade. 'win' or 'loss'."""
        if result.lower() == 'win':
            self.winning_streak += 1
            self.losing_streak = 0
        elif result.lower() == 'loss':
            self.losing_streak += 1
            self.winning_streak = 0
        else:
            raise ValueError("Result must be 'win' or 'loss'")
        
        self.history.append(result)

    def get_streaks(self):
        """Return current winning and losing streaks."""
        return self.winning_streak, self.losing_streak

    def calculate_streak_probability(self, n: int) -> (float, float):
        """Calculate the probability of a winning or losing streak of length n."""
        # Assuming a simple model of probability
        p_win = 0.5  # Replace with actual win probability if known
        p_loss = 1 - p_win
        win_prob = p_win ** n
        loss_prob = p_loss ** n
        return win_prob, loss_prob

    def analyze_patterns(self):
        """Analyze the pattern of wins and losses."""
        patterns = {}
        for i in range(len(self.history)):
            for j in range(i + 1, len(self.history) + 1):
                subsequence = tuple(self.history[i:j])
                if subsequence in patterns:
                    patterns[subsequence] += 1
                else:
                    patterns[subsequence] = 1
        return patterns
