import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Set a fixed random seed to ensure consistent results
np.random.seed(42)

class Individual:
    def __init__(self, strategy):
        self.strategy = strategy  # 'Hawk', 'Dove' or 'Mixed'

    def play(self, opponent, V, C, available_resource):
        if available_resource <= 0:
            return 0, 0  # No resources, no gain

        if self.strategy == 'Mixed':
            self_choice = np.random.choice(['Hawk', 'Dove'], p=[0.5, 0.5])
            return Individual(self_choice).play(opponent, V, C, available_resource)
        elif opponent.strategy == 'Mixed':
            opponent_choice = np.random.choice(['Hawk', 'Dove'], p=[0.5, 0.5])
            return self.play(Individual(opponent_choice), V, C, available_resource)

        if self.strategy == 'Hawk' and opponent.strategy == 'Hawk':
            return (V - C) / 2, (V - C) / 2
        elif self.strategy == 'Hawk' and opponent.strategy == 'Dove':
            return V, 0
        elif self.strategy == 'Dove' and opponent.strategy == 'Hawk':
            return 0, V
        elif self.strategy == 'Dove' and opponent.strategy == 'Dove':
            return V / 2, V / 2
        else:
            return 0, 0

class Population:
    def __init__(self, size, initial_hawk_fraction, initial_dove_fraction, initial_mixed_fraction):
        strategies = (['Hawk'] * int(size * initial_hawk_fraction) +
                      ['Dove'] * int(size * initial_dove_fraction) +
                      ['Mixed'] * int(size * initial_mixed_fraction))
        self.individuals = [Individual(strategy) for strategy in strategies]

    def evolve(self, V, C, mutation_rate, num_generations, initial_resource, renewable_resource_percent, non_renewable_resource_percent, renewable_recovery_amount):
        hawk_fractions = []
        dove_fractions = []
        mixed_fractions = []
        renewable_resources = initial_resource * renewable_resource_percent
        non_renewable_resources = initial_resource * non_renewable_resource_percent
        resources = []  # Track remaining resources each generation

        for gen in range(num_generations):
            hawk_fractions.append(sum(1 for ind in self.individuals if ind.strategy == 'Hawk') / len(self.individuals))
            dove_fractions.append(sum(1 for ind in self.individuals if ind.strategy == 'Dove') / len(self.individuals))
            mixed_fractions.append(sum(1 for ind in self.individuals if ind.strategy == 'Mixed') / len(self.individuals))

            total_resources = renewable_resources + non_renewable_resources
            if total_resources <= 0:
                total_resources = 0

            # Interaction within the population
            for i in range(len(self.individuals)):
                opponent = np.random.choice(self.individuals)
                payoff_self, payoff_opponent = self.individuals[i].play(opponent, V, C, total_resources)

                # Update resources
                total_payoff = payoff_self + payoff_opponent
                if total_payoff > 0:
                    if non_renewable_resources >= total_payoff:
                        non_renewable_resources -= total_payoff
                    else:
                        total_payoff -= non_renewable_resources
                        non_renewable_resources = 0
                        renewable_resources -= total_payoff

                # Mutation mechanism - introduce some randomness to prevent stagnation
                if np.random.rand() < mutation_rate:
                    self.individuals[i].strategy = np.random.choice(['Hawk', 'Dove', 'Mixed'])

            resources.append(total_resources)

            # Update renewable resources
            renewable_resources = min(renewable_resources + renewable_recovery_amount, initial_resource * renewable_resource_percent)

        return hawk_fractions, dove_fractions, mixed_fractions, resources

class HawkDoveApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hawk-Dove Game Simulation")
        self.geometry("800x600")

        # Inputs
        self.create_widgets()

    def create_widgets(self):
        # Input fields
        ttk.Label(self, text="Resource Value (V):").grid(row=0, column=0, padx=10, pady=5, sticky="W")
        self.v_input = ttk.Entry(self)
        self.v_input.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self, text="Fight Cost (C):").grid(row=1, column=0, padx=10, pady=5, sticky="W")
        self.c_input = ttk.Entry(self)
        self.c_input.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self, text="Population Size:").grid(row=2, column=0, padx=10, pady=5, sticky="W")
        self.pop_size_input = ttk.Entry(self)
        self.pop_size_input.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self, text="Initial Hawk Fraction:").grid(row=3, column=0, padx=10, pady=5, sticky="W")
        self.hawk_frac_input = ttk.Entry(self)
        self.hawk_frac_input.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(self, text="Initial Dove Fraction:").grid(row=4, column=0, padx=10, pady=5, sticky="W")
        self.dove_frac_input = ttk.Entry(self)
        self.dove_frac_input.grid(row=4, column=1, padx=10, pady=5)

        ttk.Label(self, text="Initial Mixed Fraction:").grid(row=5, column=0, padx=10, pady=5, sticky="W")
        self.mixed_frac_input = ttk.Entry(self)
        self.mixed_frac_input.grid(row=5, column=1, padx=10, pady=5)

        ttk.Label(self, text="Number of Generations:").grid(row=6, column=0, padx=10, pady=5, sticky="W")
        self.num_gen_input = ttk.Entry(self)
        self.num_gen_input.grid(row=6, column=1, padx=10, pady=5)

        ttk.Label(self, text="Mutation Rate:").grid(row=7, column=0, padx=10, pady=5, sticky="W")
        self.mutation_rate_input = ttk.Entry(self)
        self.mutation_rate_input.grid(row=7, column=1, padx=10, pady=5)

        ttk.Label(self, text="Initial Resource:").grid(row=8, column=0, padx=10, pady=5, sticky="W")
        self.initial_resource_input = ttk.Entry(self)
        self.initial_resource_input.grid(row=8, column=1, padx=10, pady=5)

        ttk.Label(self, text="Renewable Resource %:").grid(row=9, column=0, padx=10, pady=5, sticky="W")
        self.renewable_res_percent_input = ttk.Entry(self)
        self.renewable_res_percent_input.grid(row=9, column=1, padx=10, pady=5)

        ttk.Label(self, text="Renewable Recovery Amount:").grid(row=10, column=0, padx=10, pady=5, sticky="W")
        self.renewable_recovery_input = ttk.Entry(self)
        self.renewable_recovery_input.grid(row=10, column=1, padx=10, pady=5)

        # Run button
        self.run_button = ttk.Button(self, text="Run Simulation", command=self.run_simulation)
        self.run_button.grid(row=11, column=0, columnspan=2, pady=20)

    def run_simulation(self):
        # Collect inputs
        V = float(self.v_input.get())
        C = float(self.c_input.get())
        pop_size = int(self.pop_size_input.get())
        hawk_frac = float(self.hawk_frac_input.get())
        dove_frac = float(self.dove_frac_input.get())
        mixed_frac = float(self.mixed_frac_input.get())
        num_gen = int(self.num_gen_input.get())
        mutation_rate = float(self.mutation_rate_input.get())
        initial_resource = float(self.initial_resource_input.get())
        renewable_res_percent = float(self.renewable_res_percent_input.get())
        renewable_recovery_amount = float(self.renewable_recovery_input.get())

        # Initialize population and run simulation
        population = Population(pop_size, hawk_frac, dove_frac, mixed_frac)
        hawk_fractions, dove_fractions, mixed_fractions, resources = population.evolve(
            V, C, mutation_rate, num_gen, initial_resource, renewable_res_percent, 
            1-renewable_res_percent, renewable_recovery_amount)

        # Plot results
        self.plot_results(hawk_fractions, dove_fractions, mixed_fractions, resources)

    def plot_results(self, hawk_fractions, dove_fractions, mixed_fractions, resources):
        fig, axs = plt.subplots(2, 1, figsize=(10, 8))

        axs[0].plot(hawk_fractions, label='Hawk Fraction')
        axs[0].plot(dove_fractions, label='Dove Fraction')
        axs[0].plot(mixed_fractions, label='Mixed Fraction')
        axs[0].set_xlabel('Generation')
        axs[0].set_ylabel('Strategy Fractions')
        axs[0].legend()

        axs[1].plot(resources, label='Available Resources')
        axs[1].set_xlabel('Generation')
        axs[1].set_ylabel('Resources')
        axs[1].legend()

        plt.tight_layout()

        # Show plot in Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=12, column=0, columnspan=2, padx=10, pady=10)

if __name__ == "__main__":
    app = HawkDoveApp()
    app.mainloop()
