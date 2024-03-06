using _3semObligatoriskopgave;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _3semObligatoriskopgave
{
    public class BeersRepository
    {
        private int _nextId = 6;
        private List<Beer> _beers = new()

        {
            new Beer { Id = 1, Name = "Carlsberg", Abv = 10},
            new Beer { Id = 2, Name = "Tuborg", Abv = 20},
            new Beer { Id = 3, Name = "Pilsner", Abv = 30},
            new Beer { Id = 4, Name = "Corona", Abv = 40},
            new Beer { Id = 5, Name = "Heineken", Abv = 50},

        };

        private List<Beer> GetBeers(string? filterAbv = null, string? sortBy = null)
        {
           List<Beer> result = new List<Beer>(_beers);

           if (filterAbv != null) { }
            {
                result = result.FindAll(b => b.Name.StartsWith(filterAbv));
            } 

            if (sortBy != null)
            {
                switch (sortBy) 
                {
                    case "Name":
                        result.Sort((b1, b2) => b1.Name.CompareTo(b2.Name));
                        break;
                    case "abv":
                        result.Sort((b1,b2) => b1.Name.CompareTo(b2.Name)); 
                        break;
                
                }
            }
            return result;
        }
        public Beer? GetById(int id)
        {
            return _beers.Find(beer => beer.Id == id);
        }

        public Beer AddBeer(Beer beer)
        {
            beer.Id = _nextId++;
            _beers.Add(beer);
            return beer;

        }

        public Beer? Deletebeer(int id)
        { 
            Beer? beer = _beers.Find(beer=>beer.Id == id);
            if (beer != null) 
            {
                _beers.Remove(beer);
            }
            return beer; 
        }
        public Beer? UpdateBeer(int id, Beer data)
        {
            Beer? beerToUpdate = _beers.Find(b => b.Id == id);
            if (beerToUpdate != null) 
            {
                beerToUpdate.Name= data.Name;
                beerToUpdate.Abv = data.Abv;
            }
            return beerToUpdate;
          
            


        }
































































































    }


}

