#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Historical NBA conference playoff simulator with Tkinter."""
from __future__ import annotations
import argparse
import random
import tkinter as tk
from tkinter import ttk

EAST = (
    "Boston Celtics", "Toronto Raptors", "Cleveland Cavaliers", "Indiana Pacers",
    "Detroit Pistons", "Milwaukee Bucks", "Washington Wizards", "New York Knicks",
    "Miami Heat", "Philadelphia 76ers", "Brooklyn Nets", "Charlotte Hornets",
    "Orlando Magic", "Chicago Bulls", "Atlanta Hawks",
)
WEST = (
    "Houston Rockets", "Golden State Warriors", "San Antonio Spurs",
    "Minnesota Timberwolves", "Oklahoma City Thunder", "Denver Nuggets",
    "Portland Trail Blazers", "New Orleans Pelicans", "Utah Jazz",
    "Los Angeles Clippers", "Los Angeles Lakers", "Sacramento Kings",
    "Phoenix Suns", "Memphis Grizzlies", "Dallas Mavericks",
)

def conference_champion(teams: tuple[str, ...], rng: random.Random, lines: list[str]) -> str:
    contenders = rng.sample(teams, 8)
    while len(contenders) > 1:
        winners = []
        for a, b in zip(contenders[::2], contenders[1::2]):
            winner = rng.choice((a, b))
            lines.append(f"{a} vs {b} -> {winner}")
            winners.append(winner)
        contenders = winners
    return contenders[0]

def simulate(seed: int | None = None) -> tuple[str, list[str]]:
    rng = random.Random(seed)
    lines = ["Historical NBA fictional playoff simulation", "", "Eastern Conference"]
    east = conference_champion(EAST, rng, lines)
    lines.extend(("", "Western Conference"))
    west = conference_champion(WEST, rng, lines)
    champion = rng.choice((east, west))
    lines.extend(("", f"NBA Final: {east} vs {west}", f"Champion: {champion}"))
    return champion, lines

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text", action="store_true")
    parser.add_argument("--seed", type=int)
    args = parser.parse_args()
    def render() -> str:
        return "\n".join(simulate(args.seed)[1])
    if args.text:
        print(render())
        return
    root = tk.Tk()
    root.title("NBA Simulator — Historical Rosters")
    root.geometry("760x620")
    frame = ttk.Frame(root, padding=12)
    frame.pack(fill="both", expand=True)
    output = tk.Text(frame, wrap="word", font=("monospace", 10))
    output.pack(fill="both", expand=True)
    def refresh() -> None:
        output.delete("1.0", "end")
        output.insert("1.0", render())
    ttk.Button(frame, text="Simulate again", command=refresh).pack(pady=8)
    refresh()
    root.mainloop()

if __name__ == "__main__":
    main()
