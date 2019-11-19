import main


def test_string_to_list():
    text = """and listening to our feet slide and push across floorboards.
            Junior had a good arm, and bottles and cans rolled out from under the house
            like pool balls. They stopped when they hit the rusted-over cow bath Daddy had
            salvaged from the junkyard where he scraps metal. He’d brought it home for
            Junior’s birthday last year and told him to use it as a swimming pool.
            “Shoot,” Randall said. He was sitting on a chair under his homemade
            basketball goal, a rim he’d stolen from the county park and screwed into the
            trunk of a dead pine tree.
            “Ain’t nothing hit us in years."""
    z = main.string_to_list(text)
    assert z == text.split(" "), "Wrong!"


if __name__ == "__main__":
    test_string_to_list()
