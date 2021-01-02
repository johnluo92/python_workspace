import heapq

def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    newSchedules = joinCalendars(calendar1, calendar2)
    newDayBounds = joinDayBounds(dailyBounds1, dailyBounds2)
    while len(newSchedules):
        if newSchedules[0][1] < newDayBounds[0]:
            newSchedules.pop(0)
        else:
            break
    print([minutesToString(x) for x in newSchedules])
    print('new daily bounds:', minutesToString(newDayBounds))
    combinedCalendars = getNewCalendar(newSchedules, newDayBounds, meetingDuration)

    return combinedCalendars


def joinCalendars(cal_1, cal_2, newCal=[]):
    joinedCal = cal_1 + cal_2
    if not joinedCal:
        return []
    joinedCal = [[convertToMinutes(x) for x in time] for time in joinedCal]

    heapq.heapify(joinedCal)
    meeting1 = heapq.heappop(joinedCal)
    while len(joinedCal):
        meeting2 = heapq.heappop(joinedCal)
        print(minutesToString(meeting1), minutesToString(meeting2))
        if meeting1[1] >= meeting2[0]:
            if meeting1[1] <= meeting2[1]:
                meeting1[1] = meeting2[1]
        else:
            newCal.append(meeting1)
            meeting1 = meeting2
    newCal.append(meeting1)

    print()
    currentSchedule = [minutesToString(meeting) for meeting in newCal]
    print(currentSchedule)

    return newCal


def joinDayBounds(bound_1, bound_2):
    newStart = max(convertToMinutes(bound_1[0]), convertToMinutes(bound_2[0]))
    newEnd = min(convertToMinutes(bound_1[1]), convertToMinutes(bound_2[1]))
    return [newStart, newEnd]


def convertToMinutes(time):
    hours, minutes = list(map(int, time.split(':')))
    return (hours * 60) + minutes


def getNewCalendar(schedule, bounds, duration):
    newSchedule = []

    if schedule:
        meeting1 = schedule.pop(0)
    else:
        return [minutesToString(bounds)]

    if enoughTimeBetween(bounds[0], meeting1[0], duration):
        newSchedule.append(createNewMeeting(bounds[0], meeting1[0], duration))
    
    while len(schedule):
        meeting2 = schedule.pop(0)
        if enoughTimeBetween(meeting1[1], meeting2[0], duration):
            newSchedule.append(createNewMeeting(meeting1[1], meeting2[0], duration))
        meeting1 = meeting2
    if enoughTimeBetween(meeting1[1], bounds[1], duration):
        newSchedule.append(createNewMeeting(meeting1[1], bounds[1], duration))

    return newSchedule


def enoughTimeBetween(time1, time2, duration):
    return time2 - time1 >= duration


# create new meeting from minutes: converting from int to str array
def createNewMeeting(time1, time2, duration):
    timeInBetween = time2 - time1
    availableMinutes = (timeInBetween * duration) // duration
    endTime = time1 + availableMinutes
    newMeeting = [time1, endTime]

    return minutesToString(newMeeting)


def minutesToString(meeting):
    newSchedule = [None, None]
    i = 0
    for minutes in meeting:
        hours, minutes = divmod(minutes, 60)
        if minutes == 0:
            minutes = '00'
        newSchedule[i] = str(hours) + ':' + str(minutes)
        i += 1

    return newSchedule












calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
dailyBounds1 = ["9:00", "20:00"]
calendar2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
dailyBounds2 = ["10:00", "18:30"]
meetingDuration = 30

calendar1 = [["8:00", "10:30"], ["11:30", "13:00"], ["14:00", "16:00"], ["16:00", "18:00"]]
dailyBounds1 = ["8:00", "18:00"]
calendar2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
dailyBounds2 = ["7:00", "18:30"]
meetingDuration = 15

calendar1 = []
dailyBounds1 = ["9:30", "16:30"]
calendar2 = []
dailyBounds2 = ["9:30", "16:30"]
meetingDuration = 15

calendar1 = [
    ["7:00", "7:45"],
    ["8:15", "8:30"],
    ["9:00", "10:30"],
    ["12:00", "14:00"],
    ["14:00", "15:00"],
    ["15:15", "15:30"],
    ["16:30", "18:30"],
    ["20:00", "21:00"]
  ]
calendar2 = [
    ["9:00", "10:00"],
    ["11:15", "11:30"],
    ["11:45", "17:00"],
    ["17:30", "19:00"],
    ["20:00", "22:15"]
  ]
dailyBounds1 = ["6:30", "22:00"]
dailyBounds2 = ["8:00", "22:30"]
meetingDuration = 30


answer = calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)
print(answer)

