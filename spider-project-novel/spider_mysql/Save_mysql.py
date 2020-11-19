#encoding:utf-8
import pymysql
import time
category_name={"玄幻奇幻": 1,
"仙侠武侠": 2,
"都市言情":3,
"历史军事": 4,
"游戏竞技": 5,
"科幻末世": 6,
"悬疑推理 ":7,
"轻小说":8,}

class addMysql:
    def __init__(self):
        self.db=pymysql.connect(host ='47.106.227.43', port =3306, user = 'huanghai',passwd = 'admin888',db='api2_yqs_dev')

    def add_Mysql(self,result):
        try:
            cursor=self.db.cursor()

            category_name={"玄幻奇幻": 1,
                            "仙侠武侠": 2,
                            "都市言情":3,
                            "历史军事": 4,
                            "游戏竞技": 5,
                            "科幻末世": 6,
                            "悬疑推理 ":7,
                            "轻小说":8,}
            status={"完结":0,"连载":1}
                            # sql = 'insert into topnews(author, title, url, publishedAt,AddOn) values ("%s","%s","%s","%s","%s")' % (author, title, url, publishedAt, AddOn);
            # sql="INSERT INTO `api2_yqs_dev`.`novel_category`(`name`) VALUES (category_name[result[category]])"
            sql="select * from novel where title=%s and author=%s "
            cursor.execute(sql,[result['title'],result['author']])
            res=cursor.fetchall()

            if not res:
                #插入小说基础数据表
                sql="INSERT INTO `api2_yqs_dev`.`novel`(`title`,`author`, `category_id`, `cover`, `introduction`, `nums`, `status`, `updated_at`, `created_at`, `url`, `source`) VALUES ('%s','%s', %d, '%s', '%s', %s, %s, '%s', %s, '%s', '%s')"%(result["title"],result['author'],category_name[result['category']],result["cover"],result["introduction"],result["nums"],status[result["status"]],result['update'],int(time.time()),result["url"],'17K')
                print(sql)
                cursor.execute(sql)
                self.db.commit()
                novel_id=cursor.lastrowid

            sql="select url from novel_chapter where  url=%s "
            cursor.execute(sql,[result['data']['url']])
            res=cursor.fetchall()

            if not res:
                #插入小说章节数据表
                sql="select id from novel where title=%s and author=%s "
                cursor.execute(sql,[result['title'],result['author']])
                res=cursor.fetchall()
                novel_id=res[0][0]

                sql="INSERT INTO `api2_yqs_dev`.`novel_chapter`(`novel_id`, `title`, `url`) VALUES ( '%s', '%s', '%s')"%(novel_id,result['data']['title1'],result['data']['url'])
                print(sql)
                cursor.execute(sql)
                self.db.commit()
                #插入小说章节内容表
                chapter_id=cursor.lastrowid
                sql="INSERT INTO `api2_yqs_dev`.`novel_article`(`chapter_id`, `content`, `create_at`) VALUES (%s, '%s', %s)"%(chapter_id,result["data"]["content"],int(time.time()),)
                print(sql)
                cursor.execute(sql)
                self.db.commit()
            return 0

        except Exception as e:
            print(e)
            self.db.rollback()
            return 1
if __name__ =='__main__':
    result={
                    'author': '米五糖',
                    'category': '玄幻奇幻',
                    'cover': 'http://cdn.static.17k.com/book/189x272/81/22/3232281.jpg-189x272?v=0',
                    'introduction': '    宇宙物质，存在必有其规律，生命是物质规律下的特殊产物，不同规律产生出不同的生物，他们生活在不同的世界，过着不一样的生活。生物不断进化，出现了智慧生命，以智慧触摸宇宙规律，使文明进步，使自身强大。追逐永恒不灭，追逐掌控命运是所有生命的共同心愿，却又难以实现。科技、修行尽皆坎坷，利用好命运赋予的资源，完成应尽的使命，永恒与掌控也许真的会实现。',
                    'nums': '55114',
                    'status': '连载',
                    'title': '寰宇新星',
                    'update': '2020-10-26 10:19',
                    'url': 'https://www.17k.com/book/3232281.html',
                    'data': {
                        'title1': '时空',
                        'content': '<p>时间学和空间学都很深奥，天文学又以光年为距离单位，茫茫宇宙，人类极其渺小，但人的思维却无限大。我总在想在特定的环境，以人的智商一定会找到真正的修炼之法，而这个特定的环境，也许和我们在同一时空，也许在我们不可捉摸的其它时空。</p><p>假如真的有那么一些世界，可以让自己强大，可以活得更长，谁愿意离开现在生活的世界呢？</p>',
                        'url': 'https://www.17k.com/chapter/3232281/41633839.html'
                    }
                }
    mysql=Mysql()
    mysql.add_Mysql(result)