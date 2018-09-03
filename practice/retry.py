import time


def retry_test(given):
    flag = given  # Try input bound integers (given ± 1)
    cnt = 0
    for _ in range(given):
        cnt += 1
        try:
            if cnt is flag:
                print('success')
                break
            else:
                3 // 0  # Error excepted.
        except:
            print('error')
            time.sleep(1)

        if cnt is given:
            print(f"Retry {given} all times.")


retry_test(given=5)
