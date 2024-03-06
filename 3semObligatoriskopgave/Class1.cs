namespace _3semObligatoriskopgave
{
    public class Beer
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public double Abv { get; set; }
        //Abv = Alcohol by volume

        public override string ToString()
        {
            return $"{Name}, {Abv}";
        }

        public void ValidateName()
        {
            if (Name != null)
            {
                throw new ArgumentNullException("Name må ikke være null");
            }
            if (Name.Length < 5)
            {
                throw new ArgumentNullException("Name skal være mindst 5 tegn  langt");
            }

        }

        public void ValidateAbv()
        {
            if (Abv < 0 || Abv > 70)
            {
                throw new ArgumentOutOfRangeException("Abv skal være mellem 0 og 70");

            }
        }

        




    }
}