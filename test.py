import sys
import json
import os
import subprocess
import platform

# testcase 저장 파일 경로
testcaseFilePath = "./testcase/testcase.json"


def run_test(file_path, i, v, sample_input, sample_output):
    pythonVersion = 'python' if v else 'python3'
    try:
        # 파일 경로의 파이썬 파일을 subprocess로 open
        file = subprocess.Popen(
            [pythonVersion, file_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    except Exception as err:
        print("파일이 존재하지 않습니다.", err)
        return -1

    # subprocess 실행된 파일에 sample_input 전달
    file.communicate(input=bytes(str(sample_input).rstrip(), encoding="utf-8"))

    # subprocess 실행된 파일의 출력을 가져옴
    result, err = file.communicate()

    print(f"테스트케이스({i})")
    # 에러가 발생했을 경우 -1 반환
    err = err.decode('utf-8')
    if err == '':
        result = result.decode('utf-8').rstrip()
    else:
        print("Error\n", err)
        return -1

    print(f"입력 예시: {sample_input}")
    print(f"출력 예시: {sample_output}\n출력 결과: {result}")
    if str(sample_output).rstrip() == result:
        print("   [통과]   ")
        print("-----------")
        return 1
    else:
        print("   [실패]   ")
        print("-----------")
        return 0


def getTestCase(problem_number):  # json 파일에 해당 문제 testcase들을 가져와 반환
    try:
        with open(testcaseFilePath, "r") as json_file:
            problem_testcase = json.load(json_file)[problem_number]
    except Exception as err:
        print(f"{problem_number}은 테스트 케이스에 존재하지 않는 문제번호입니다.", err)
        return -1
    return problem_testcase


def main():
    # 문제 번호 및 이름 입력
    print("problem: ", end="")
    sys.stdout.flush()  # 버퍼 내리기
    problem_number = sys.stdin.readline().rstrip()
    print("name: ", end="")
    sys.stdout.flush()
    name = sys.stdin.readline().rstrip()
    name = name.lower()
    if name == 'j' or name == 'jeonhui':
        name = 'Jeonhui'
    elif name == 'g' or name == 'gyeongrok':
        name = 'Gyeongrok'
    else:
        print("등록되지 않은 사용자입니다.")
        return

    pv = False if platform.system() == 'Darwin' else True

    # 파일 경로 설정
    file_path = os.path.join(os.getcwd(), name, 'problem', problem_number + ".py")

    # 테스트 케이스 가져오기
    testcases = getTestCase(problem_number)
    if testcases == -1:
        return

    # 테스트 케이스를 성공적으로 가져왔을 경우
    print("-----------")
    print(f"문제 이름: {problem_number}")
    print("-----------")
    i = 1
    for key in testcases.keys():
        if run_test(file_path, i, pv, key, testcases[key]) == -1:
            return
        i += 1


main()
