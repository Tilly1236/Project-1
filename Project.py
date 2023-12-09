import tkinter as tk

class VotingSystemGUI:
    def __init__(self, master):
        """
        Initialize the VotingSystemGUI.

        Parameters:
            master (tk.Tk): The master Tkinter window.
         """
        self.master = master
        self.master.title("Voting for Jane or John!=")
        self.master.geometry('500x500')
        self.total_num = 0
        self.vote_john = 0
        self.vote_jane = 0

        self.create_widgets()

    def create_widgets(self):
        """
        Create and pack the main widgets in the GUI.
        """
        self.vote_button = tk.Button(self.master, text="Vote", command=self.show_vote_menu)
        self.vote_button.pack(pady=10)

        self.exit_button = tk.Button(self.master, text="Exit", command=self.display_results)
        self.exit_button.pack(pady=10)

    def show_vote_menu(self):
        """
        Display the vote menu window.
        """
        vote_menu_window = tk.Toplevel(self.master)
        vote_menu_window.title("Vote Menu")

        vote_label = tk.Label(vote_menu_window, text="Do you want to vote?")
        vote_label.pack(pady=10)

        vote_button = tk.Button(vote_menu_window, text="Vote", command=self.show_candidate_menu)
        vote_button.pack(pady=5)

    def show_candidate_menu(self):
        """
        Display the candidate menu window.
        """
        candidate_menu_window = tk.Toplevel(self.master)
        candidate_menu_window.title("Candidate Menu")

        candidate_label = tk.Label(candidate_menu_window, text="Who do you want to vote for?")
        candidate_label.pack(pady=10)

        john_button = tk.Button(candidate_menu_window, text="John", command=lambda: self.process_vote(1))
        john_button.pack(pady=5)

        jane_button = tk.Button(candidate_menu_window, text="Jane", command=lambda: self.process_vote(2))
        jane_button.pack(pady=5)

    def process_vote(self, candidate: int):
        """
        Process the vote for a candidate.

        Parameters:
            candidate (int): The candidate selected (1 for John, 2 for Jane).
        """
        if candidate == 1:
            print('Voted John')
            self.vote_john += 1
        elif candidate == 2:
            print('Voted Jane')
            self.vote_jane += 1

        self.total_num += 1

    def display_results(self):
        """
        Display the voting results window.
        """
        result_window = tk.Toplevel(self.master)
        result_window.title("Voting Results")

        result_label = tk.Label(result_window, text=f'John-{self.vote_john}, Jane-{self.vote_jane}, Total-{self.total_num}')
        result_label.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = VotingSystemGUI(root)
    root.mainloop()
