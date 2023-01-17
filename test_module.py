import unittest
import demographic_data_analyzer

class DemographicAnalyzerTestCase(unittest.TestCase):
    def setUp(self):
        self.data = demographic_data_analyzer.calculate(print_data = False)

    def test_q1_race(self):
        actual = self.data['q1_race'].tolist()
        expected = [27816, 3124, 1039, 311, 271]
        self.assertAlmostEqual(actual, expected, "Expected race count values to be [27816, 3124, 1039, 311, 271]")
    
    def test_q2_avg_men(self):
        actual = self.data['q2_avg_men']
        expected = 39.4
        self.assertAlmostEqual(actual, expected, "Expected different value for average age of men.")

    def test_q3_percentage_bachelors(self):
        actual = self.data['q3_percentage_bachelors']
        expected = 16.4 
        self.assertAlmostEqual(actual, expected, "Expected different value for percentage with Bachelors degrees.")

    def test_q4_adv_more50k(self):
        actual = self.data['q4_adv_more50k']
        expected = 10.7
        self.assertAlmostEqual(actual, expected, "Expected different value for percentage with higher education that earn >50K.")
  
    def test_q5_noadvedu_more50k(self):
        actual = self.data['q5_noadvedu_more50k']
        expected = 13.4
        self.assertAlmostEqual(actual, expected, "Expected different value for percentage without higher education that earn >50K.")

    def test_q6_min_hours(self):
        actual = self.data['q6_min_hours']
        expected = 1.0
        self.assertAlmostEqual(actual, expected, "Expected different value for minimum work hours.")     

    def test_q7_minhr_more50k(self):
        actual = self.data['q7_minhr_more50k']
        expected = 0.0
        self.assertAlmostEqual(actual, expected, "Expected different value for percentage of rich among those who work fewest hours.")   

    def test_q8_highest_country(self):
        actual = self.data['q8_highest_country']
        expected = 'United-States'
        self.assertAlmostEqual(actual, expected, "Expected different value for highest earning country.")   

    def test_q8_percentage(self):
        actual = self.data['q8_percentage']
        expected = 22.0
        self.assertAlmostEqual(actual, expected, "Expected different value for heighest earning country percentage.")   

    def test_q9_pop_occupation(self):
        actual = self.data['q9_pop_occupation']
        expected = 'Exec-managerial'
        self.assertEqual(actual, expected, "Expected different value for top occupations in India.")      

if __name__ == "__main__":
    unittest.main()

