def greet(name):
    """주어진 이름으로 간단한 인사말을 출력합니다."""
    return f"안녕하세요, {name}님! 파이썬 예제입니다."


def main():
    이름 = "사용자"
    메시지 = greet(이름)
    print(메시지)


if __name__ == "__main__":
    main()
