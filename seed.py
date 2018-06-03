from sqlalchemy import func
from model import User, Address, Profile, Diet, UserDiet, Favorite, Visit, Rating, Restaurant
from datetime import date


from model import connect_to_db, db
from server import app


def load_diets():
    """ Load the diets into the DB """

    print "Diets"

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    Diet.query.delete()

    DIETS = ['vegan', 'vegetarian', 'gluten_free', 'kosher', 'halal']

    for item in DIETS:

        diet = Diet(diet_name=item)

        # We need to add to the session or it won't ever be stored
        db.session.add(diet)

    # Once we're done, we should commit our work
    db.session.commit()

def load_profiles():
    """ Load the user profiles into the DB """

    print "Profiles"

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    Profile.query.delete()

    PROFILES = {'foodie': ['spicy', 'salty', 'sweet', 'umami']


                            # {'taste': ['spicy', 'salty', 'sweet', 'umami']}
                # 'starving student': [
                #                     {'price':'1'}
                #                     ],
                # 'health nut': [
                #             {'diet_restrict': ['vegan', 'gluten_free']}
                #             ],
                # 'heat seaker': [
                #                 {'taste': ['spicy']},
                #                 {'temp': ['hot']}
                #             ]
                }

    for name, definition in PROFILES.items():

        profile = Profile(type_name=name, type_define=definition)

        # We need to add to the session or it won't ever be stored
        db.session.add(profile)

    # Once we're done, we should commit our work
    db.session.commit()


def load_ratings():
    """ Load the ratings into the DB """

    print "Ratings"

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    Rating.query.delete()

    SCORES = [1, 2, 3, 4, 5]

    for num in SCORES:
        score = Rating(score=num)

        # We need to add to the session or it won't ever be stored
        db.session.add(score)

    # Once we're done, we should commit our work
    db.session.commit()

def sample_user():
    """ Add sample user to DB """

    print "Sample User"

    alyssa = User(first_name="Alyssa", last_name= "Lew", email="alyssa@example.com", password="123", user_type_id=1)
    db.session.add(alyssa)
    db.session.commit()


def sample_address():
    """ Add sample address to DB """

    print "Sample Address"

    a1 = Address(user_id=1, address_label='hackbright', address='683 Sutter St, San Francisco, CA 94109')
   
    db.session.add(a1)
    db.session.commit()


def sample_user_diet():
    """ Add sample address to DB """

    print "Sample User Diet"

    u_diet = UserDiet(user_id=1, diet_id=2)

    db.session.add(u_diet)
    db.session.commit()

def sample_restaurant():
    """ Add sample restaurant to DB """

    print "Sample Restaurant"

    restaurant = Restaurant(yelp_biz_id='wGl_DyNxSv8KUtYgiuLhmA', name='Bi-Rite Creamery')

    db.session.add(restaurant)
    db.session.commit()

def sample_visit():
    """ Add sample visit to DB """

    print "Sample Visit"

    today = date.today()
    v = Visit(user_id=1, restaurant_id=1, rating_id=5, visit_date=today)
    db.session.add(v)
    db.session.commit()


def sample_favorite():
    """ Add sample favorite to DB """

    print "Sample Favorite"

    fav = Favorite(user_id=1, restaurant_id=1, favorite=True)
    db.session.add (fav)
    db.session.commit()




if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Import different types of data
    load_diets()
    load_profiles()
    load_ratings()

    sample_user()
    sample_address()
    sample_user_diet()
    sample_restaurant()
    sample_visit()
    sample_favorite()


