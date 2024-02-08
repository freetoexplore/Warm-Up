asteroids = [10, 2, -5]
initial_len = len(asteroids)
negative = 0
while True:
    if len(asteroids) == initial_len:
        
        for a in asteroids:
            if a < 0:
                negative = 1
                a = abs(a)
        
                if a < asteroids[asteroids.index(-a) - 1]:
                    asteroids = [i for i in asteroids if i != -a]
                elif a == asteroids[asteroids.index(-a) - 1]:
                    asteroids = [i for i in asteroids if i != -a and i != a]
                elif a > asteroids[asteroids.index(-a) - 1] :
                    asteroids = [i for i in asteroids if i != asteroids[asteroids.index(-a) - 1] ]
                    
    elif len(asteroids) != initial_len:
        for a in asteroids:
            if a < 0:
                negative = 1
                a = abs(a)
        
                if a < asteroids[asteroids.index(-a) - 1]:
                    asteroids = [i for i in asteroids if i != -a]
                elif a == asteroids[asteroids.index(-a) - 1]:
                    asteroids = [i for i in asteroids if i != -a and i != a]
                elif a > asteroids[asteroids.index(-a) - 1] :
                    asteroids = [i for i in asteroids if i != a ]
        break

        
print(asteroids)        
