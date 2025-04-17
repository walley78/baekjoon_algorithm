from collections import defaultdict

def solution(points, routes):
    # 포인트 번호를 좌표로 매핑
    point_dict = {i + 1: tuple(coord) for i, coord in enumerate(points)}
    
    # 시간대별 좌표에 로봇 수를 기록
    time_position_map = defaultdict(lambda: defaultdict(int))
    
    for route in routes:
        # 시작 위치
        x, y = point_dict[route[0]]
        time = 0
        time_position_map[time][(x, y)] += 1
        
        # 경로를 따라 이동
        for idx in range(1, len(route)):
            target_x, target_y = point_dict[route[idx]]
            
            # r 좌표를 먼저 맞춤
            while x != target_x:
                x += 1 if target_x > x else -1
                time += 1
                time_position_map[time][(x, y)] += 1
            
            # c 좌표를 맞춤
            while y != target_y:
                y += 1 if target_y > y else -1
                time += 1
                time_position_map[time][(x, y)] += 1
    
    # 충돌 위험 계산
    collision_count = 0
    for positions in time_position_map.values():
        for count in positions.values():
            if count > 1:
                collision_count += 1
                
    return collision_count
