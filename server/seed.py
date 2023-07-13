#!/usr/bin/env python3

from faker import Faker
from random import randint, choice as rc

from config import app, db

from models.author import Author
from models.book import Book
from models.quote import Quote
from models.shelf import Shelf
from models.tag import Tag
from models.user import User

from models.book_shelf import BookShelf
from models.book_tag import BookTag
from models.review import Review


fake = Faker()

with app.app_context(): 

    print("Deleting all records ...")

    Author.query.delete()
    Book.query.delete()
    Quote.query.delete()
    Shelf.query.delete()
    Tag.query.delete()
    User.query.delete()

    BookShelf.query.delete()
    BookTag.query.delete()
    Review.query.delete()

    # Creating initial tables 

    print("Creating authors ...")
    a1 = Author(full_name="Amy Gerstler", bio=fake.paragraph())
    a2 = Author(full_name="R.F. Kuang", bio=fake.paragraph())
    a3 = Author(full_name="Richard Powers", bio=fake.paragraph())
    a4 = Author(full_name="Edward Albee", bio=fake.paragraph())
    a5 = Author(full_name="Maurice Sendak", bio=fake.paragraph())
    a6 = Author(full_name="Meg Wolitzer", bio=fake.paragraph())
    a7 = Author(full_name="Gerda Weissmann Klein", bio=fake.paragraph())
    authors = [a1, a2, a3, a4, a5, a6, a7]
    db.session.add_all(authors)

    print("Creating books ...")
    genres = ["Poetry", "Fantasy", "Historical Fiction", "Memoir", 
                "Literary Fiction", "Horror", "Drama", "Children's"]
    
    b1 = Book(
        title="Dearest Creature",
        description="""
            Hallucinogenic plants chant in chorus. A thoughtful dog grants an interview. A caterpillar offers life advice. Amy Gerstler’s newest collection of poetry, Dearest Creature, marries fact and fiction in a menagerie of dramatic monologues, twisted love poems, and epistolary pleadings. Drawing on sources as disparate as Lewis Carroll and Mary Shelley’s Frankenstein, as well as abnormal psychology, etiquette, and archaeology texts, these darkly imaginative poems probe what it means to be a sentient, temporary, flesh-and-blood beast, to be hopelessly, vividly creaturely.
        """, 
        genre="Poetry",
        page_count=96,
        cover_photo="https://m.media-amazon.com/images/I/91NTy5MeveL._SY522_.jpg",
        author=a1
    )

    b2 = Book(
        title="The Poppy War",
        description="""
            When Rin aced the Keju—the Empire-wide test to find the most talented youth to learn at the Academies—it was a shock to everyone: to the test officials, who couldn’t believe a war orphan from Rooster Province could pass without cheating; to Rin’s guardians, who believed they’d finally be able to marry her off and further their criminal enterprise; and to Rin herself, who realized she was finally free of the servitude and despair that had made up her daily existence. That she got into Sinegard—the most elite military school in Nikan—was even more surprising.

            But surprises aren’t always good.

            Because being a dark-skinned peasant girl from the south is not an easy thing at Sinegard. Targeted from the outset by rival classmates for her color, poverty, and gender, Rin discovers she possesses a lethal, unearthly power—an aptitude for the nearly-mythical art of shamanism. Exploring the depths of her gift with the help of a seemingly insane teacher and psychoactive substances, Rin learns that gods long thought dead are very much alive—and that mastering control over those powers could mean more than just surviving school.

            For while the Nikara Empire is at peace, the Federation of Mugen still lurks across a narrow sea. The militarily advanced Federation occupied Nikan for decades after the First Poppy War, and only barely lost the continent in the Second. And while most of the people are complacent to go about their lives, a few are aware that a Third Poppy War is just a spark away . . .

            Rin’s shamanic powers may be the only way to save her people. But as she finds out more about the god that has chosen her, the vengeful Phoenix, she fears that winning the war may cost her humanity . . . and that it may already be too late.
        """, 
        genre="Fantasy",
        page_count=544,
        cover_photo="https://m.media-amazon.com/images/I/415sNT7bPjL._SY445_SX342_.jpg",
        author=a2
    )

    b3 = Book(
        title="The Dragon Republic",
        description="""
            The war is over.

            The war has just begun.

            Three times throughout its history, Nikan has fought for its survival in the bloody Poppy Wars. Though the third battle has just ended, shaman and warrior Rin cannot forget the atrocity she committed to save her people. Now she is on the run from her guilt, the opium addiction that holds her like a vice, and the murderous commands of the fiery Phoenix—the vengeful god who has blessed Rin with her fearsome power.

            Though she does not want to live, she refuses to die until she avenges the traitorous Empress who betrayed Rin’s homeland to its enemies. Her only hope is to join forces with the powerful Dragon Warlord, who plots to conquer Nikan, unseat the Empress, and create a new republic.

            But neither the Empress nor the Dragon Warlord are what they seem. The more Rin witnesses, the more she fears her love for Nikan will force her to use the Phoenix’s deadly power once more.

            Because there is nothing Rin won’t sacrifice to save her country . . . and exact her vengeance.
        """, 
        genre="Fantasy",
        page_count=672,
        cover_photo="https://m.media-amazon.com/images/I/41B7aPHTmvL._SY445_SX342_.jpg",
        author=a2
    )
    

    b4 = Book(
        title="The Burning God",
        description="""
            After saving her nation of Nikan from foreign invaders and battling the evil Empress Su Daji in a brutal civil war, Fang Runin was betrayed by allies and left for dead.

            Despite her losses, Rin hasn’t given up on those for whom she has sacrificed so much—the people of the southern provinces and especially Tikany, the village that is her home. Returning to her roots, Rin meets difficult challenges—and unexpected opportunities. While her new allies in the Southern Coalition leadership are sly and untrustworthy, Rin quickly realizes that the real power in Nikan lies with the millions of common people who thirst for vengeance and revere her as a goddess of salvation.

            Backed by the masses and her Southern Army, Rin will use every weapon to defeat the Dragon Republic, the colonizing Hesperians, and all who threaten the shamanic arts and their practitioners. As her power and influence grows, though, will she be strong enough to resist the Phoenix’s intoxicating voice urging her to burn the world and everything in it? 
        """, 
        genre="Fantasy",
        page_count=656,
        cover_photo="https://m.media-amazon.com/images/I/71pNOR-3x3L._SY522_.jpg",
        author=a2
    )
    
    b5 = Book(
        title="The Overstory",
        description="""
            The Overstory, winner of the 2019 Pulitzer Prize in Fiction, is a sweeping, impassioned work of activism and resistance that is also a stunning evocation of―and paean to―the natural world. From the roots to the crown and back to the seeds, Richard Powers’s twelfth novel unfolds in concentric rings of interlocking fables that range from antebellum New York to the late twentieth-century Timber Wars of the Pacific Northwest and beyond. There is a world alongside ours―vast, slow, interconnected, resourceful, magnificently inventive, and almost invisible to us. This is the story of a handful of people who learn how to see that world and who are drawn up into its unfolding catastrophe.
        """, 
        genre="Literary Fiction",
        page_count=512,
        cover_photo="https://m.media-amazon.com/images/I/81YgPnTNf5L._SY522_.jpg",
        author=a3
    )

    b6 = Book(
        title="Who's Afraid of Virginia Woolf?",
        description="""
            “Twelve times a week,” answered actress Uta Hagen when asked how often she’d like to play Martha in Who’s Afraid of Virginia Woolf? In the same way, audiences and critics alike could not get enough of Edward Albee’s masterful play. A dark comedy, it portrays husband and wife George and Martha in a searing night of dangerous fun and games. By the evening’s end, a stunning, almost unbearable revelation provides a climax that has shocked audiences for years. With its razor-sharp dialogue and the stripping away of social pretense, Newsweek rightly foresaw Who’s Afraid of Virginia Woolf? as “a brilliantly original work of art—an excoriating theatrical experience, surging with shocks of recognition and dramatic fire [that] will be igniting Broadway for some time to come.”
        """, 
        genre="Drama",
        page_count=272,
        cover_photo="https://m.media-amazon.com/images/I/81lKVMC0SxL._SY522_.jpg",
        author=a4
    )

    b7 = Book(
        title="Where the Wild Things Are",
        description="""
            This iconic story has inspired a movie, an opera, and the imagination of generations. When Max dresses in his wolf suit and causes havoc in the house, his mother sends him to bed. From there, Max sets sail to an island inhabited by the Wild Things, who name him king and share a wild rumpus with him. But then from far away across the world, Max smells good things to eat...
        """, 
        genre="Children's",
        page_count=48,
        cover_photo="https://m.media-amazon.com/images/I/61AmMPEa1SL._SY522_.jpg",
        author=a5
    )

    b8 = Book(
        title="The Interestings",
        description="""
            The summer that Nixon resigns, six teenagers at a summer camp for the arts become inseparable. Decades later the bond remains powerful, but so much else has changed. In The Interestings, Wolitzer follows these characters from the height of youth through middle age, as their talents, fortunes, and degrees of satisfaction diverge.

            The kind of creativity that is rewarded at age fifteen is not always enough to propel someone through life at age thirty; not everyone can sustain, in adulthood, what seemed so special in adolescence. Jules Jacobson, an aspiring comic actress, eventually resigns herself to a more practical occupation and lifestyle. Her friend Jonah, a gifted musician, stops playing the guitar and becomes an engineer. But Ethan and Ash, Jules’s now-married best friends, become shockingly successful—true to their initial artistic dreams, with the wealth and access that allow those dreams to keep expanding. The friendships endure and even prosper, but also underscore the differences in their fates, in what their talents have become and the shapes their lives have taken.

            Wide in scope, ambitious, and populated by complex characters who come together and apart in a changing New York City, The Interestings explores the meaning of talent; the nature of envy; the roles of class, art, money, and power; and how all of it can shift and tilt precipitously over the course of a friendship and a life.
        """, 
        genre="Literary Fiction",
        page_count=460,
        cover_photo="https://m.media-amazon.com/images/I/51uL9I-u3EL._SY445_SX342_.jpg",
        author=a6
    )

    b9 = Book(
        title="All But My Life",
        description="""
            From her comfortable home in Bielitz (present-day Bielsko) in Poland to her miraculous survival and her liberation by American troops--including the man who was to become her husband--in Volary, Czechoslovakia, in 1945, Gerda takes the reader on a terrifying journey.

            Gerda's serene and idyllic childhood is shattered when Nazis march into Poland on September 3, 1939. Although the Weissmanns were permitted to live for a while in the basement of their home, they were eventually separated and sent to German labor camps. Over the next few years Gerda experienced the slow, inexorable stripping away of "all but her life." By the end of the war she had lost her parents, brother, home, possessions, and community; even the dear friends she made in the labor camps, with whom she had shared so many hardships, were dead.

            Despite her horrifying experiences, Klein conveys great strength of spirit and faith in humanity. In the darkness of the camps, Gerda and her young friends manage to create a community of friendship and love. Although stripped of the essence of life, they were able to survive the barbarity of their captors. Gerda's beautifully written story gives an invaluable message to everyone. It introduces them to last century's terrible history of devastation and prejudice, yet offers them hope that the effects of hatred can be overcome.
        """, 
        genre="Memoir",
        page_count=272,
        cover_photo="https://m.media-amazon.com/images/I/41OxmraY4wL._SY445_SX342_.jpg",
        author=a7
    )

    books = [b2, b3, b4, b1, b5, b6, b7, b8, b9]
    
    db.session.add_all(books)

    print("Creating quotes ...")
    quotes = []
    for _ in range(50): 
        quote = Quote(
            content=fake.paragraph(),
            book = rc(books)
        )
        quotes.append(quote)

    db.session.add_all(quotes)

    # print("Creating tags ...")
    # tags = []
    # for _ in range(10): 
    #     tag = Tag(
    #         name=fake.sentence(nb_words=1)
    #     )
    #     tags.append(tag)
    
    # db.session.add_all(tags)

    print("Creating users ...")
    users = []
    usernames = []
    emails = []

    for _ in range(15):
        username = fake.first_name()
        email = fake.email()

        while username in usernames:
            username = fake.first_name()
        usernames.append(username)

        while email in emails: 
            email = fake.email()
        emails.append(email)

        user = User(
            username=username,
            email=email,
            profile_pic=fake.image_url(),
            display_name=fake.first_name(),
            bio=fake.paragraph()
        )
        user.password_hash = user.username + "password"

        users.append(user)

    db.session.add_all(users)

    print("Creating shelves ...")
    shelves = []
    for user in users: 
        s1 = Shelf(
            name="Read",
            user=user
        )
        s2 = Shelf(
            name="Want to read",
            user=user
        )
        s3 = Shelf(
            name="Favorites",
            user=user
        )
        shelves.extend([s1, s2, s3])
    
    db.session.add_all(shelves)

    # Creating join tables 
    print("Creating book_shelves ...")
    book_shelves = []

    for shelf in shelves: 
        for _ in range(5):
            book_shelf = BookShelf(
                book=rc(books),
                shelf=shelf,
                user=shelf.user
            )
            book_shelves.append(book_shelf)

    db.session.add_all(book_shelves)

    # print("Creating book_tags ...")
    # book_tags = []

    # for _ in range(50):
    #     book_tag = BookTag(
    #         book=rc(books),
    #         tag=rc(tags)
    #     )
    #     book_tags.append(book_tag)
    
    # db.session.add_all(book_tags)

    # print("Creating reviews ...")
    # reviews = []
    
    # for _ in range(50):
    #     review = Review(
    #         rating=randint(0,5),
    #         comment=fake.paragraph(),
    #         book=rc(books),
    #         user=rc(users)
    #     )
    #     reviews.append(review)

    # db.session.add_all(reviews)

    print("Committing to db ...")

    db.session.commit()

    print("Complete")