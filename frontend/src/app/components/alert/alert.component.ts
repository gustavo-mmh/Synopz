import { Component, Input, OnInit, OnChanges, SimpleChanges } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-alert',
  templateUrl: './alert.component.html',
  styleUrls: ['./alert.component.scss'],
  standalone: true,
  imports: [CommonModule]
})
export class AlertComponent implements OnInit, OnChanges {
  @Input() message: string = '';
  @Input() type: 'success' | 'error' = 'success';
  @Input() isVisible: boolean = true;
  progress: number = 100;

  ngOnInit(): void {
    this.startCountdown();
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['message'] || changes['type']) {
      this.isVisible = true;
      this.progress = 100;
      this.startCountdown();
    }
  }

  startCountdown(): void {
    const interval = setInterval(() => {
      this.progress -= 2;
      if (this.progress <= 0) {
        clearInterval(interval);
        this.isVisible = false;
      }
    }, 100);
  }
}
