from vpython import *

earth = sphere(pos=vec(0, 0, 0), radius=6400000, texture=textures.earth)
moon = sphere(pos=vec(385000000, 0, 0), radius=1737100,
              texture=textures.rock, make_trail=True)

# 지구와 달의 확대를 위한 설정
earth.radius = 6 * earth.radius
moon.radius = 6 * moon.radius

# 각종 상수
G = 6.673e-11
earth.m = 5.972e24
moon.m = 7.347e22

# 초기 위치 설정
earth.pos = vec(0, 0, 0)
moon.pos = vec(385000000, 0, 0)

# 초기 속도 설정
earth.v = vec(0, 0, 0)
moon.v = vec(0, 1022, 0)

# 1 프레임당 시뮬레이션에서는 60초가 지나간다는 설정
# 즉, rate(1000)일 때 1초가 지나면 60000초가 지남 
t = 0
dt = 60

while True:
    rate(1000)

    r = moon.pos - earth.pos

    # 만유인력 법칙과 작용과 반작용의 법칙
    moon.f = -G * earth.m * moon.m/mag(r)**2*norm(r)
    earth.f = -moon.f

    # F = m*a를 이용해 a 구하기
    moon.v = moon.v + moon.f/moon.m * dt
    earth.v = earth.v + earth.f/earth.m * dt

    moon.pos = moon.pos + moon.v * dt
    earth.pos = earth.pos + earth.v * dt

    t = t + dt

