from captcha_solver import CaptchaSolver

solver = CaptchaSolver('captcha', api_key='1abc234de56fab7c89012d34e56fa7b8')

raw_data = open('captcha.png', 'rb').read()

print(solver.solve_captcha(raw_data))