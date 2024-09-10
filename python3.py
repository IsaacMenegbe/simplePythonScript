
profile = {
    'name': 'Isaac Menegbe',
    'coaahort': '4',
    'track': 'Software Development ',
    'powered_by': 'PORA Academy'
}

for key, value in profile.items():
    print(f'{key}: {value}\n')


name = input("what is your fullname?" )

while True:
    
    try:
        cohort = int(input( "which cohort are you (enter a number) :"))
        
        break
    except ValueError :
        
        print("invalid input.  Please enter a number for this cohort")
         
learning_track = input ("what is your learning track")

print(f'my name is {name}, \ni am in cohort {cohort} \nand my learning track is{learning_track}')


