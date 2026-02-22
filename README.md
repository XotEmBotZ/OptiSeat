# OptiSeat 🏛️

**An algorithmic optimization engine for complex institutional seating arrangements.**

OptiSeat is a high-performance Python application designed to solve the "combinatorial bottleneck" of exam and classroom seating. It replaces manual, error-prone processes with a deterministic allocation algorithm that ensures optimal resource utilization while maintaining strict academic integrity constraints.

## 🧠 The Algorithm: First Principles Allocation

OptiSeat doesn't just "place students in rooms." It employs a multi-pass allocation logic that handles:
- **Relational Constraints:** Links students, subjects, sections, and room capacities via a structured SQLite schema.
- **Dynamic Capacity Management:** Handles variable bench counts and student-per-bench densities.
- **Sequential Integrity:** Automatically detects and optimizes for sequential roll numbers to simplify post-allocation logistics.
- **Multi-Date Orchestration:** Processes multiple exam dates and subject pairs in a single execution loop.

## ✨ Key Features

- **Automated Seat Allocation:** Greedy-based optimization for filling rooms based on subject and section priority.
- **Relational Data Engine:** Powered by SQLite for robust, local-first data persistence.
- **Post-Processing Intelligence:** Converts raw allocation data into "Instruction Sets" (Range-based or Array-based) for easier implementation by invigilators.
- **Streamlit GUI:** A modern, reactive interface for data input and visualization.
- **Sequence Detection:** Identifies continuous roll number blocks (`isSeq` logic) to reduce the complexity of seating charts.

## 🛠️ Tech Stack

- **Language:** [Python 3.10+](https://www.python.org/)
- **Frontend:** [Streamlit](https://streamlit.io/)
- **Database:** [SQLite3](https://www.sqlite.org/)
- **Data Analysis:** [Pandas](https://pandas.pydata.org/)
- **Serialization:** [Pickle](https://docs.python.org/3/library/pickle.html) for fast binary state recovery.

## 🚀 Getting Started

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/XotEmBotZ/OptiSeat.git
   cd OptiSeat
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## 📊 Logic Overview (`allocateSeat`)
The core engine iterates through distinct dates and subject pairings. It maintains a stateful `studLst` and fills rooms sequentially while validating against `numBench` and `benchStud` constraints. If a room cannot accommodate the required density, the algorithm raises an `AssertionError`, ensuring no "overflow" or illegal seating occurs.

## 💡 Use Case
Perfect for schools, colleges, and competitive exam centers that need to generate high-integrity seating plans for 1000+ students across multiple rooms and subjects in seconds.
