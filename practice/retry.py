import time

given = 5

print('[test00]')


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
            print(cnt)
            print(f"Retry {given} all times.")


retry_test(given)

print('[test01]')


def retry_test_idx(given):
    flag = given  # Try input bound integers (given ± 1)
    for i, _ in enumerate(range(given), start=1):
        try:
            if i is flag:
                print('success')
                break
            else:
                3 // 0  # Error excepted.
        except:
            print('error')
            time.sleep(1)

        if i is given:
            print(i)
            print(f"Retry {given} all times.")


retry_test_idx(given)
