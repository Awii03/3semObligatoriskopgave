﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _3semObligatoriskopgave
{
    public partial class Test : Component
    {
        public Test()
        {
            InitializeComponent();
        }

        public Test(IContainer container)
        {
            container.Add(this);

            InitializeComponent();
        }
    }
}
