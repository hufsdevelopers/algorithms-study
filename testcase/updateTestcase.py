import json

# testcase 저장 파일 경로
import sys

updateFilePath = "./update.txt"
testcaseFilePath = "./testcase.json"


def borrowFile(problem_number):
    updateFile = open(updateFilePath, 'w')
    updateFile.write(f"problem {problem_number}\n")
    try:
        testcase = getTestCase()[problem_number]
        i = 1
        for key in testcase.keys():
            updateFile.write(f"input{i}\n{key}\n\noutput{i}\n{testcase[key]}\n\n")
            i += 1
    except:
        updateFile.write(f"input1\n\n\noutput1\n\n")
    updateFile.close()


def updateFile():
    testcases = getTestCase()
    updateFile = open(updateFilePath, 'r')
    title = updateFile.readline().split()
    if len(title) != 2:
        print("문제 번호가 입력되지 않았습니다.")
        return -1
    else:
        mode = True
        problem_number = title[1]
        answer = ""
        key = None
        value = None
        if problem_number not in testcases.keys():
            testcases[problem_number] = {}
        for line in updateFile:
            if line.rstrip()[:5] == "input" or line[:5].rstrip() == "예제 입력":
                mode = True
            elif line.rstrip()[:6] == "output" or line[:5].rstrip() == "예제 출력":
                mode = False

            elif line.rstrip() != "":
                answer += line
            else:
                if mode:
                    key = answer.rstrip()
                else:
                    value = answer.rstrip()
                    if key is not None or (key != "" and value != ""):
                        testcases[problem_number][key] = value
                    key = None
                answer = ""
        if key is not None and (key != "" and value != ""):
            testcases[problem_number][key] = value
        with open(testcaseFilePath, 'w') as f:
            json.dump(testcases, f, indent='\t')


def deleteData(problem_number, testcaseInput):
    testcases = getTestCase()
    if problem_number in testcases.keys():
        if testcaseInput in testcases[problem_number].keys():
            testcases[problem_number].pop(testcaseInput)
        else:
            print("해당 문제의 테스트 케이스가 존재하지 않습니다.")
            return -1
    else:
        print("해당 문제가 존재하지 않습니다.")
        return -1
    with open(testcaseFilePath, 'w') as f:
        json.dump(testcases, f, indent='\t')


def deleteProblem(problem_number):
    testcases = getTestCase()
    if problem_number in testcases.keys():
        testcases.pop(problem_number)
    else:
        print("해당 문제가 존재하지 않습니다.")
        return -1
    with open(testcaseFilePath, 'w') as f:
        json.dump(testcases, f, indent='\t')


def getTestCase():  # json 파일에 해당 문제 testcase들을 가져와 반환
    try:
        with open(testcaseFilePath, "r") as json_file:
            problem_testcase = json.load(json_file)
    except Exception as err:
        print(err)
        return -1
    return problem_testcase


def printTestcase(problem_number):
    testcases = getTestCase()
    if problem_number in testcases.keys():
        print("-----------")
        print(f"문제 번호: {problem_number}")
        print("-----------")
        i = 1
        for key in testcases[problem_number].keys():
            print(f"input{i}\n{key}\n\noutput{i}\n{testcases[problem_number][key]}")
            print("-----------")
            i += 1
    else:
        print("해당 문제가 존재하지 않습니다.")
        return -1


def main():
    print("파일로 불러오기(0) / 파일 업데이트(1) / 테스트케이스 삭제(2) / 문제 삭제(3) / 테스트케이스 출력 (4)\n입력: ", end="")
    mode = int(sys.stdin.readline())

    if mode == 0:
        print("문제 번호: ", end="")
        problem_number = sys.stdin.readline().rstrip()
        borrowFile(problem_number)

    elif mode == 1:
        updateFile()

    elif mode == 2:
        print("문제 번호: ", end="")
        problem_number = sys.stdin.readline().rstrip()
        print("테스트케이스 입력: ", end="")
        testcaseInput = sys.stdin.readline().rstrip()
        deleteData(problem_number, testcaseInput)

    elif mode == 3:
        print("문제 번호: ", end="")
        problem_number = sys.stdin.readline().rstrip()
        deleteProblem(problem_number)

    elif mode == 4:
        print("문제 번호: ", end="")
        problem_number = sys.stdin.readline().rstrip()
        printTestcase(problem_number)


main()
