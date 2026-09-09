#
# bmi 계산 함수
# 

def get_bmi(weight:float, height:float) -> float:
    bmi = weight_kg / (height_cm / 100) ** 2
    return bmi
def test_get_bmi():
    wight_kg = 66
    height_cm = 172
    h = get_bmi(66,172)
    print(f"키(height_cm),몸무게(weight_kg)의 bmi는 {h}입니다.")

    if __name__ == "__main__":
        test_get_bmi()
