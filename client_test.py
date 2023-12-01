import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    expected_output =[
       ('ABC', 120.48, 121.2, (120.48 + 121.2)/2),
       ('DEF', 117.87, 121.68, (117.87 + 121.68)/2)
    ]

    for i in range(len(quotes)):
       self.assertEqual(getDataPoint(quotes[i]), expected_output[i])
    
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
          ]
    expected_output = [
      ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2),
      ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
          ]
    for i in range(len(quotes)):
      self.assertEqual(getDataPoint(quotes[i]), expected_output[i])

  """ ------------ Add more unit tests ------------ """

  def test_getDataPoint_missingFields(self):
    quote = {'top_ask': {'price': 121.2}, 'timestamp': '2019-02-11 22:06:30.572453', 'stock': 'ABC'}  # missing 'size' and 'top_bid'
    with self.assertRaises(KeyError):
      getDataPoint(quote)

  def test_getDataPoint_emptyQuote(self):
    quote = {}
    with self.assertRaises(KeyError):
      getDataPoint(quote)

  def test_getDataPoint_identicalBids(self):
    quotes = [
      {'top_ask': {'price': 120.5, 'size': 50}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.5, 'size': 100}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 115.0, 'size': 40}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 115.0, 'size': 80}, 'id': '0.109974697771', 'stock': 'DEF'}
      ]
    expected_output = [
      ('ABC', 120.5, 120.5, 120.5),
      ('DEF', 115.0, 115.0, 115.0)
    ]
    for i in range(len(quotes)):
      self.assertEqual(getDataPoint(quotes[i]), expected_output[i])



if __name__ == '__main__':
    unittest.main()
