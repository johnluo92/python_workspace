import heapq

def scheduler(meetings):

     my_meetings = meetings[:]
     new_schedule = collapseIntervals(my_meetings)

     return new_schedule

def collapseIntervals(intervals):
     heapq.heapify(intervals)
     # print(intervals)
     current = heapq.heappop(intervals)
     new_schedule = []

     while intervals:
          next_meeting = heapq.heappop(intervals)

          if current[1] >= next_meeting[0]:
               if current[1] < next_meeting[1]:
                    current[1] = next_meeting[1]
          else:
               new_schedule.append(current)
               current = next_meeting
          
          if not intervals:
               new_schedule.append(current)

     return new_schedule

sample_meetings = [[1,5],[2,5],[3,6],[9,10],[7,9],[11,12]]
sample_answer = [[1,6],[7,10],[11,12]]

meetings = [[21,22],[1,4],[2,3],[4,6],[7,8],[9,10],[16,20],[15,18]]
answer = [[1,6],[7,8],[9,10],[15,20],[21,22]]

meetings1 = [[0,1],[2,5],[9,12],[1,6],[2,3],[4,5],[7,10],[10,11],[10,12],[15,20]]
answer1 = [[0, 6], [7, 12], [15, 20]]

meetings2 = [[1,2],[3,4],[5,6],[7,8]]
answer2 = [[1, 2], [3, 4], [5, 6], [7, 8]]

meetings3 = [[10,20],[15,20],[18,25],[9,15],[5,22]]
answer3 = [[5, 25]]

import unittest
class TestProgram(unittest.TestCase):
     def test_case_0(self):
          self.assertEqual(scheduler(sample_meetings), sample_answer)
     def test_case_1(self):
          self.assertEqual(scheduler(meetings), answer)
     def test_case_2(self):
          self.assertEqual(scheduler(meetings1), answer1)
     def test_case_3(self):
          self.assertEqual(scheduler(meetings2), answer2)
     def test_case_4(self):
          self.assertEqual(scheduler(meetings3), answer3)
unittest.main()