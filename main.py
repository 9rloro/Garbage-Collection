import gc

# 가비지 컬렉션 활성화
gc.enable()

# 클래스 정의
class MyClass:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Deleting instance {self.name}")

# 객체 생성
obj1 = MyClass("Object 1")
obj2 = MyClass("Object 2")

# 순환 참조 생성 (obj1이 obj2를 참조하고, obj2가 obj1을 참조)
obj1.other = obj2
obj2.other = obj1

# 객체에 대한 참조 해제 (순환 참조가 해결되지 않음)
obj1 = None
obj2 = None

# 가비지 컬렉션 실행
gc.collect()
