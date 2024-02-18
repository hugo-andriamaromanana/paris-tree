import pandas as pd
import googlemaps as gmaps
from pathlib import Path
from math import sqrt

from ..consts import GOOGLE_API_KEY, DEFAULT_TRANSPORTATION_MODE
from ..data_classes import Treater, Tree, Quest, Coordinates


def initialize_googlemaps_client(api_key: str = GOOGLE_API_KEY):
    """
    Initializes and returns the Google Maps API client.
    """
    return gmaps.Client(key=api_key)


def convert_df_to_trees(trees_csv_path: Path) -> list[Tree]:
    all_trees = []
    df = pd.read_csv(trees_csv_path)
    for column in df:
        all_trees.append(
            Tree(
                id=column["id"],
                coordinates=Coordinates(
                    x=column["geo_point_2d_a"], y=column["geo_point_2d_b"]
                ),
            )
        )
    return all_trees

def calculate_distance(coord1: Coordinates, coord2: Coordinates) -> float:
    """
    Calculates the Euclidean distance between two coordinates.
    """
    return sqrt((coord1.x - coord2.x)**2 + (coord1.y - coord2.y)**2)

def assign_closest_tree(coordinate: Coordinates, all_trees: list[Tree]) -> Tree:
    """
    Assigns the closest tree to the given coordinate from the list of trees.
    """
    closest_tree = min(all_trees, key=lambda tree: calculate_distance(coordinate, tree.coordinates))
    return closest_tree

def initialize_treaters(
    treaters: list[Treater], all_trees: list[Tree]
) -> list[Treater]:
    """
    uses the assign closest tree function to do it on every treater.
    """
    for treater in treaters:
        treater.closest_tree = assign_closest_tree(treater.starting_position, all_trees)
    return treaters

def generate_quests(
    available_treaters: list[Treater], all_trees: list[Tree]
) -> list[Quest]:
    """
    Complex stuff here
    """
    # Goes through all the available trees and tries to assign ALL the trees
    # To every available treaters
    # The function will take into input all the starting positions (so a treater), and assign them a list of trees to cover whilst respecting a tree_treated, distance_covered ratio
    pass


def main(tree_csv_path: Path, available_treaters: list[Treater]) -> dict[str, Quest]:
    all_trees = convert_df_to_trees(tree_csv_path)
    available_treaters = assign_closest_tree(available_treaters)
    quests = generate_quests(available_treaters, all_trees)
    planning = {}
    for quest in quests:
        planning[quest.treater_id] = quest.missions
    return planning