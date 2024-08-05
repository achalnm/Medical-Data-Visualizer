import unittest
import pandas as pd
from medical_data_visualizer import preprocess_data, draw_cat_plot, draw_heat_map

class TestMedicalDataVisualizer(unittest.TestCase):
    def setUp(self):
        self.df = preprocess_data()

    def test_overweight_column(self):
        self.assertIn('overweight', self.df.columns)
        self.assertTrue((self.df['overweight'].isin([0, 1])).all())

    def test_normalize_columns(self):
        self.assertTrue((self.df['cholesterol'].isin([0, 1])).all())
        self.assertTrue((self.df['gluc'].isin([0, 1])).all())

    def test_cat_plot(self):
        fig = draw_cat_plot()
        self.assertIsNotNone(fig)

    def test_heat_map(self):
        fig = draw_heat_map()
        self.assertIsNotNone(fig)

if __name__ == '__main__':
    unittest.main()
