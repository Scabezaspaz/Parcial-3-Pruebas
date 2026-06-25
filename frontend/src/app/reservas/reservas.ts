import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-reservas',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './reservas.html',
  styleUrl: './reservas.css'
})
export class ReservasComponent {
  email = '';
  zona = 'VIP';
  cantidad = 1;
  total = 0;

  readonly precios: Record<string, number> = {
    VIP: 150000,
    General: 50000
  };

  confirmarReserva() {
    this.total = this.cantidad * this.precios[this.zona];
  }
}