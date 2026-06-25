import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { ReservasComponent } from './reservas/reservas';
import { provideAnimations } from '@angular/platform-browser/animations';
import { LOCALE_ID } from '@angular/core';
import { registerLocaleData } from '@angular/common';
import localeEs from '@angular/common/locales/es';

registerLocaleData(localeEs);

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter([
      { path: 'reservas', component: ReservasComponent },
      { path: '', redirectTo: 'reservas', pathMatch: 'full' }
    ]),
    { provide: LOCALE_ID, useValue: 'es' }
  ]
};