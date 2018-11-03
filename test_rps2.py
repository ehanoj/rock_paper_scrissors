import rps2
import subprocess
import sys

def test_rock_is_valid_play():
    assert rps2.is_valid_play('rock') is True

def test_paper_is_valid_play():
    assert rps2.is_valid_play('paper') is True

def test_scissors_is_valid_play():
    assert rps2.is_valid_play('scissors') is True
    
def test_lizard_is_invalid_play():
    assert rps2.is_valid_play('lizard') is False

def test_computer_play_is_valid():
    for _ in range(5000):
        play = rps2.generate_computer_play()
        assert rps2.is_valid_play(play)

def test_computer_plays_randomly():
    plays = [rps2.generate_computer_play() for _ in range(1000)]
    r = plays.count('rock') 
    p = plays.count('paper')
    s = plays.count('scissors')
    print(r, p, s)
    assert r > 300
    assert p > 300
    assert s > 300

def test_paper_beats_rock():
    result = rps2.evaluate_game('paper', 'rock')
    assert result == 'human'

def input_faked_rock(prompt):
    print(prompt)
    return 'paper'

def test_full_game(capsys):
    rps2.main(inputusr=input_faked_rock)
    captured = capsys.readouterr()
    assert 'rock, paper, or scissors?' in captured.out

def test_wrong_play_result_in_reated_question():
    cp = subprocess.run([sys.executable, 'rps2.py'], encoding='utf-8', stdout=subprocess.PIPE, input='dragon\nrock\n', check=True)
    assert cp.stdout.count('rock, paper, or scissors?') == 2
