from collections import deque

from codeit_kr.bfs import station as a


def bfs(start: a.Station, goal: a.Station, stations: dict):
    previous_stations = stations
    queue = deque
    current = None

    start.previous = None
    queue.append(start)

    """
    # 변수 정의
    previous 사전 생성
    queue 생성
    current = None

    # 초기 설정
    start의 previous를 None로 설정
    queue에 start 추가

    아직 보지 않은 역이 있고, 도착역을 찾지 않았을 경우 반복:
        queue의 앞에 있는 역 빼서 current에 지정

        current의 neighbor를 순서대로 본다:
            neighbor가 아직 안 본 역이면:
                queue에 추가한다
                previous 사전에 추가한다

    만약 current가 goal이면:
        경로를 만들어서 리턴

    current가 goal이 아니면 None을 리턴
    """
