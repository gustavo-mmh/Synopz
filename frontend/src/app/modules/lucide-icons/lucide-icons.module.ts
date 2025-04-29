import { NgModule } from '@angular/core';
import { LucideAngularModule } from 'lucide-angular';
import { PlayCircle, KeyRound, FileText, Bot, Copy, FileDown, Download } from 'lucide'; // <- CORRETO! Agora sim

@NgModule({
  imports: [
    LucideAngularModule.pick({ PlayCircle, KeyRound, FileText, Bot, Copy, FileDown, Download })
  ],
  exports: [
    LucideAngularModule
  ]
})
export class LucideIconsModule { }
