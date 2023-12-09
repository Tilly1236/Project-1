from typing import Union


class VotingSystem:
    def __init__(self):
        self.total_num = 0
        self.vote_john = 0
        self.vote_jane = 0

    def vote_menu(self) -> str:
        """
        Display the vote menu and get user input.

        Returns:
           str: User's choice ('v' for vote, 'x' for exit).
        """
        print('---------------------------')
        print("VOTE MENU")
        print('---------------------------')
        print('v: Vote')
        print('x: Exit')
        your_vote = input('Do you want to vote? (v/x):').strip().lower()

        while True:
            if your_vote == 'v' or your_vote == 'x':
                return your_vote
            else:
                your_vote = input('Invalid (v/x):').strip().lower()

    def candidate_menu(self) -> int:
        """
        Display the candidate menu and get user's candidate choice.

        Returns:
           int: User's candidate choice (1 for John, 2 for Jane).
        """
        print('---------------------')
        print('CANDIDATE MENU')
        print('----------------------')
        print('1: John')
        print('2: Jane')
        your_cand = int(input('Who do you want to vote for? (1/2):'))

        while True:
            if your_cand == 1 or your_cand == 2:
                return your_cand
            else:
                your_cand = int(input('Invalid (1/2):'))

    def main(self):
        while True:
            your_main = self.vote_menu()
            if your_main == 'x':
                self.display_results()
                break
            elif your_main == 'v':
                your_cand = self.candidate_menu()
                self.process_vote(your_cand)

    def process_vote(self, candidate: int):
        """
        Process the user's vote and update the vote counts.

        Args:
           candidate (int): User's candidate choice (1 for John, 2 for Jane).
        """
        if candidate == 1:
            print('Voted John')
            self.vote_john += 1
            self.total_num += 1
        elif candidate == 2:
            print('Voted Jane')
            self.vote_jane += 1
            self.total_num += 1

    def display_results(self):
        """
        Display the voting results.
        """
        print('-------------------------')
        print(f'John-{self.vote_john}, Jane-{self.vote_jane}, Total-{self.total_num}')
        print('-------------------------')


if __name__ == "__main__":
    voting_system = VotingSystem()
    voting_system.main()

