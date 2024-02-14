from config import app

from models import *

if __name__ == "__main__":
  with app.app_context():
    
    print("Clearing out tables...")

    Alchemist.query.delete()
    Recipe.query.delete()

    print('Seeding classes table...')
    
    new_alchemist_1 = Alchemist(
      name = "Jabir ibn Hayyan",
      experienceLevel = 3,
      recipe_number = 1
    )

    db.session.add(new_alchemist_1)
    db.session.commit()

    new_alchemist_2 = Alchemist(
      name = "Ge Hong",
      experienceLevel = 2,
      recipe_number = 2
    )

    db.session.add(new_alchemist_2)
    db.session.commit()

    new_alchemist_3 = Alchemist(
      name = "Nicolas Flamel",
      experienceLevel = 1,
      recipe_number = 3
    )

    db.session.add(new_alchemist_3)
    db.session.commit()

    new_alchemist_4 = Alchemist(
      name = "Avicenna",
      experienceLevel = 4,
      recipe_number = 4
    )

    db.session.add(new_alchemist_4)
    db.session.commit()

    new_recipe = Recipe(
      name = "Philosopher's Stone",
      alchemistID = new_alchemist_1.id,
      ingredients = "Red Lion, White Eagle",
      description = "The Philosopher's Stone, an elusive substance, is theorized to be produced through the alchemical marriage of the Red Lion (Mercuric Oxide) and the White Eagle (Aqua Regia), representing the conjunction of the sun and moon. It's said to grant eternal life and turn base metals into gold."
    )

    db.session.add(new_recipe)
    db.session.commit()

    new_recipe = Recipe(
      name = "Aqua Regia",
      alchemistID = new_alchemist_1.id,
      ingredients = "Aqua Fortis, Spirits of Salt",
      description = "Aqua Regia, a potent alchemical mixture, is created by combining one part Aqua Fortis (Nitric Acid) with three parts Spirit of Salt (Hydrochloric Acid), known for its unique ability to dissolve the noble metal gold, symbolizing the ultimate transmutation."
    )

    db.session.add(new_recipe)
    db.session.commit()

    new_recipe = Recipe(
      name = "Aether of Clarity",
      alchemistID = new_alchemist_1.id,
      ingredients = "Cinnabar, Azoth, Aqua Vitae",
      description = "A mystic concoction offering visions of divine truth, blending Cinnabar for transformation, Azoth as the essence of life, and Aqua Vitae for rejuvenation and enlightenment."
    )

    db.session.add(new_recipe)
    db.session.commit()

    new_recipe = Recipe(
      name = "Golden Elixir",
      alchemistID = new_alchemist_2.id,
      ingredients = "Lead, Mercury",
      description = "The Golden Elixir, also known as Jindan, involves the alchemical combination of Lead and Mercury. This process, symbolizing the union of yin (lead) and yang (mercury), was aimed at creating an internal alchemical transformation within the practitioner, leading towards spiritual immortality rather than physical alchemy."
    )

    db.session.add(new_recipe)
    db.session.commit()

    new_recipe = Recipe(
      name = "Lunar Caustic",
      alchemistID = new_alchemist_3.id,
      ingredients = "Silver, Spirit of Nitre",
      description = "Lunar Caustic, known for its medicinal and magical properties, is made by dissolving Silver in Spirit of Nitre (Nitric Acid), resulting in Silver Nitrate. This compound was historically used for its antiseptic qualities and to create magical mirrors."
    )

    db.session.add(new_recipe)
    db.session.commit()

    new_recipe = Recipe(
      name = "Oil of Vitriol",
      alchemistID = new_alchemist_1.id,
      ingredients = "Green Vitriol",
      description = "Oil of Vitriol is produced by distilling Green Vitriol (Iron(II) Sulfate) and yields Sulfuric Acid. This powerful acid was used in various alchemical operations, symbolizing the dissolution and transformation of substances."
    )

    db.session.add(new_recipe)
    db.session.commit()

    new_recipe = Recipe(
      name = "Aqua Fortis",
      alchemistID = new_alchemist_3.id,
      ingredients = "Saltpeter, Vitriol",
      description = "Aqua Fortis, or strong water, is created by distilling a mixture of Saltpeter (Potassium Nitrate) and Vitriol (Sulfuric Acid), producing Nitric Acid. This acid was widely used in alchemy for dissolving metals and preparing other compounds."
    )

    db.session.add(new_recipe)
    db.session.commit()

    new_recipe = Recipe(
      name = "Immortality Wine",
      alchemistID = new_alchemist_2.id,
      ingredients = "Rice Wine, Ginseng, Goji Berries",
      description = "This more benign concoction involves infusing Rice Wine with Ginseng and Goji Berries. Unlike the more dangerous mineral-based elixirs, this wine was believed to strengthen the body, enhance longevity, and balance the spiritual energies, embodying a holistic approach to alchemy."
    )

    db.session.add(new_recipe)
    db.session.commit()

    new_recipe = Recipe(
      name = "Healing Balm",
      alchemistID = new_alchemist_4.id,
      ingredients = "Rose Water, Olive Oil, Beeswax",
      description = "Drawing from medical expertise, this healing balm uses Rose Water (for its soothing properties), Olive Oil (as a base), and Beeswax (to create a protective barrier). This concoction reflects an approach to medicine, combining practical remedies with the underlying philosophical principles of healing and balance."
    )

    db.session.add(new_recipe)
    db.session.commit()

    new_recipe = Recipe(
      name = "Alchemical Ink",
      alchemistID = new_alchemist_4.id,
      ingredients = "Soot, Gallnuts, Vinegar",
      description = "This recipe for an alchemical ink, used for writing important manuscripts and texts, combines Soot (for pigment), Gallnuts (as a binding agent), and Vinegar (to preserve and enhance the ink's durability). It symbolizes the transmission of knowledge."
    )
    db.session.add(new_recipe)
    db.session.commit()

    new_recipe = Recipe(
      name = "Memory Elixir",
      alchemistID = new_alchemist_4.id,
      ingredients = "Ginkgo Biloba, Rosemary, Green Tea",
      description = "An elixir to enhance memory and cognitive function, combining Ginkgo Biloba (to increase blood flow to the brain), Rosemary (traditionally associated with memory improvement), and Green Tea (for its antioxidant properties)."
    )

    db.session.add(new_recipe)
    db.session.commit()