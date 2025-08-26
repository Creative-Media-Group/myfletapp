import flet as ft
from flet_notifications import LocalNotifications, NotificationAction


async def main(page: ft.Page):
    # Initialize notifications
    notifications = LocalNotifications()
    page.overlay.append(notifications)

    # Create notification actions
    accept_action = NotificationAction(id="accept", title="Accept")
    decline_action = NotificationAction(id="decline", title="Decline", destructive=True)

    # Show notification with actions
    await notifications.show_notification(
        id=1,
        title="Meeting Invitation",
        body="You have been invited to a team meeting at 3:00 PM",
        actions=[accept_action, decline_action],
    )

    # Handle notification action responses
    def on_notification_action(e):
        action_id = e.data["actionId"]
        if action_id == "accept":
            page.snack_bar = ft.SnackBar(content=ft.Text("Meeting accepted!"))
            page.snack_bar.open = True
        elif action_id == "decline":
            page.snack_bar = ft.SnackBar(content=ft.Text("Meeting declined!"))
            page.snack_bar.open = True
        page.update()

    # Subscribe to notification action events
    notifications.on_notification_action = on_notification_action


ft.app(main)
