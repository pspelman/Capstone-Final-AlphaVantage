from django.test import TestCase, Client
from django.urls import reverse, resolve
from get_stocks.views import stock_list
from get_stocks.views_search import view_search_stock, display_stock_data_
from get_stocks.views_saved import view_saved_stock
from get_stocks.models import FindStock


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.stock_search = FindStock.objects.create(
            Symbol = 'MSFT',
            Interval = '5min'
        )


    def test_view_url_exists_at_HOME_PAGE_GET(self):

        response = self.client.get(reverse('get_stocks:stock_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'get_stocks/home.html')


    def test_view_url_exists_at_SEARCHSTOCKS_GET(self):

        response = self.client.get(reverse('get_stocks:view_search_stock'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'get_stocks/searchStocks/searchstocks.html')


    def test_view_url_exists_at_SAVEDSTOCKS_Output_GET(self):

        response = self.client.get(reverse('get_stocks:view_stock'))

        self.assertEqual(response.status_code, 200)

        #Changed urls (really should be get_stocks/savedstocks/savedstocks.html)
        #Possible reroute 
        self.assertTemplateUsed(response, 'get_stocks/searchStocks/searchstocks.html')


    # def test_view_search_DISPLAY_STOCK_DATA_POST(self):

    #     ui_input = self.stock_search

    #     response = self.client.post('get_stocks:view_stock', {
    #         'Symbol':'MSFT',
    #         'Interval':'5min'
    #     })

    #     print(response)
    #     self.assertEquals(response.status_code, 302)




    







