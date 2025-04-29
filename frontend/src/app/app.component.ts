import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { VideoSummarizerComponent } from './components/video-summarizer/video-summarizer.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  standalone: true,
  imports: [CommonModule, VideoSummarizerComponent] // Importe os módulos necessários aqui
})
export class AppComponent {
  title = 'Resumidor de Vídeos';
}
