import unittest
from unittest.mock import patch, mock_open
import json
from utils.data_loader import load_products, filter_products_by_category

class TestDataLoader(unittest.TestCase):
    
    def setUp(self):
        """테스트 설정"""
        self.sample_products = [
            {
                "uuid": "test-1",
                "name": "테스트 상품 1",
                "category": "food_agriculture",
                "location_code": "KR-26-16"
            },
            {
                "uuid": "test-2", 
                "name": "테스트 상품 2",
                "category": "food_fishery",
                "location_code": "KR-26-12"
            }
        ]
    
    @patch('builtins.open', new_callable=mock_open)
    @patch('json.load')
    def test_load_products_success(self, mock_json_load, mock_file):
        """상품 로드 성공 테스트"""
        mock_json_load.return_value = self.sample_products
        
        result = load_products()
        
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['name'], '테스트 상품 1')
    
    def test_filter_products_by_category(self):
        """카테고리별 필터링 테스트"""
        result = filter_products_by_category(self.sample_products, 'food_agriculture')
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['category'], 'food_agriculture')

if __name__ == '__main__':
    unittest.main()
