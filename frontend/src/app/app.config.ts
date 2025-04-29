import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter([]), // Configure as rotas aqui, se necessário
    provideHttpClient() // Fornece o cliente HTTP
  ]
};
