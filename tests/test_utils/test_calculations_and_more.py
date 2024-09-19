from app.utils.calculations_and_more import *

sample_data = [
    {"playerName": "John", "season": 2021, "position": "Guard"},
    {"playerName": "Mike", "season": 2021, "position": "Forward"},
    {"playerName": "John", "season": 2020, "position": "Guard"},
    {"playerName": "Chris", "season": 2020, "position": "Forward"},
    {"playerName": "Mike", "season": 2019, "position": "Guard"},
]


def test_filter_by_season():
    assert filter_by_season(sample_data, 2021) == [
        {"playerName": "John", "season": 2021, "position": "Guard"},
        {"playerName": "Mike", "season": 2021, "position": "Forward"}
    ]
    assert filter_by_season(sample_data, 2020) == [
        {"playerName": "John", "season": 2020, "position": "Guard"},
        {"playerName": "Chris", "season": 2020, "position": "Forward"}
    ]
    assert filter_by_season(sample_data, 2019) == [
        {"playerName": "Mike", "season": 2019, "position": "Guard"}
    ]


def test_filter_by_position():
    assert filter_by_position(sample_data, "Guard") == [
        {"playerName": "John", "season": 2021, "position": "Guard"},
        {"playerName": "John", "season": 2020, "position": "Guard"},
        {"playerName": "Mike", "season": 2019, "position": "Guard"}
    ]
    assert filter_by_position(sample_data, "Forward") == [
        {"playerName": "Mike", "season": 2021, "position": "Forward"},
        {"playerName": "Chris", "season": 2020, "position": "Forward"}
    ]


def test_filter_by_name():
    assert filter_by_name(sample_data, "John") == [
        {"playerName": "John", "season": 2021, "position": "Guard"},
        {"playerName": "John", "season": 2020, "position": "Guard"}
    ]
    assert filter_by_name(sample_data, "Mike") == [
        {"playerName": "Mike", "season": 2021, "position": "Forward"},
        {"playerName": "Mike", "season": 2019, "position": "Guard"}
    ]
    assert filter_by_name(sample_data, "Chris") == [
        {"playerName": "Chris", "season": 2020, "position": "Forward"}
    ]


def test_list_of_names():
    assert set(list_of_names(sample_data)) == {"John", "Mike", "Chris"}


def test_seasons_player():
    assert seasons_player(sample_data, "John") == "2021, 2020"
    assert seasons_player(sample_data, "Mike") == "2021, 2019"
    assert seasons_player(sample_data, "Chris") == "2020"
