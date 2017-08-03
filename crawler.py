from icrawler.builtin import GoogleImageCrawler

def google_image_crawl(directory='lena', keyword='lena', max_num=500):
    google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                                        storage={'root_dir': directory})
    google_crawler.crawl(keyword=keyword, max_num=max_num,
                         date_min=None, date_max=None,
                         min_size=(200,200), max_size=None)

google_image_crawl(directory='audi_q7', keyword='audi q7') 
google_image_crawl(directory='hyundai_porter', keyword='hyundai porter') 
google_image_crawl(directory='tesla_model_x', keyword='tesla model X') 
google_image_crawl(directory='kia_stinger', keyword='kia stinger') 
