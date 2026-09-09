def say_happy_birthday(name: str) -> None:
    print("안녕하세요")
    print(name + "님의 생일을 축하합니다")
    return None
def test_say_happy_birthday() -> None:
    say_happy_birthday("태현")
    say_happy_birthday("재균")
    say_happy_birthday("기범")

def test_say_happy_birthday2():
    nmaes = ["태현", "재균", "기범"]
    for name in nmaes:
        say_happy_birthday(name)

    def test_say_happy_birthday3():   
    say_happy_birthday(3.14)
    say_happy_birthday(100)
    say_happy_birthday([1,2,3])

if __name__ == "__main__":
    test_say_happy_birthday3()