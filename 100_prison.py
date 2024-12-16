import random
def simulate_100_prisoners_problem(num_trials):
    success_count = 0
    
    for _ in range(num_trials):
        boxes = list(range(1, 101))
        random.shuffle(boxes)
        
        all_success = True
        for prisoner in range(1, 101):
            opened_count = 0
            current_box = prisoner
            
            while opened_count < 50:
                opened_count += 1
                current_box = boxes[current_box - 1]  
                
                if current_box == prisoner:
                    break
            else:
                all_success = False
                break
        
        if all_success:
            success_count += 1

    
    success_probability = success_count / num_trials
    return success_probability


n = 10000  
success_rate = simulate_100_prisoners_problem(n)
print(f"{n}번 시뮬레이션에서 성공 확률: {success_rate:.4f}")
